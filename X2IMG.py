import os
import glob
import tkinter as tk
os.environ['PATH'] += f";{os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dlls')}"
import cairosvg
from PIL import Image, ImageTk
import base64
import io
import svgwrite
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
base64_icon = "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"

def select_files():
    paths = filedialog.askopenfilenames(title='Select Image Files', filetypes=[("Image Files", "*.svg;*.png;*.gif;*.jpg;*.jpeg;*.bmp;*.tiff;*.webp;*.ico")])
    if paths: 
        selected_files_label.config(text=f"Selected Files: {len(paths)}")
        global selected_image_files
        selected_image_files = paths

def select_folder():
    folder = filedialog.askdirectory(title='Select a Folder with Image Files')
    if folder:
        image_files = glob.glob(os.path.join(folder, '*.svg')) + glob.glob(os.path.join(folder, '*.png')) + \
                      glob.glob(os.path.join(folder, '*.gif')) + glob.glob(os.path.join(folder, '*.jpg')) + \
                      glob.glob(os.path.join(folder, '*.jpeg')) + glob.glob(os.path.join(folder, '*.bmp')) + \
                      glob.glob(os.path.join(folder, '*.tiff')) + glob.glob(os.path.join(folder, '*.webp')) + \
                      glob.glob(os.path.join(folder, '*.ico'))
        if image_files: 
            selected_files_label.config(text=f"Selected Files: {len(image_files)}")
            global selected_image_files
            selected_image_files = image_files

def convert_to_base64(image_file, output_folder):
    with open(image_file, "rb") as img_file:
        base64_string = base64.b64encode(img_file.read()).decode('utf-8')
    base64_file_path = os.path.join(output_folder, 'converted', os.path.basename(image_file).replace(os.path.splitext(image_file)[1], '.base64'))
    with open(base64_file_path, "w") as base64_file:
        base64_file.write(base64_string)

def convert_to_svg(image_file, img, output_folder):
    width, height = img.size
    svg_file_path = os.path.join(output_folder, 'converted', os.path.splitext(os.path.basename(image_file))[0] + '.svg')
    dwg = svgwrite.Drawing(svg_file_path, profile='tiny', size=(width, height))
    for y in range(height):
        for x in range(width):
            r, g, b, a = img.getpixel((x, y))
            if a > 0:  
                dwg.add(dwg.rect(insert=(x, y), size=(1, 1), fill=svgwrite.rgb(r, g, b, '%')))
    dwg.save()

def process_images(image_files):
    output_folder = os.getcwd()
    os.makedirs(os.path.join(output_folder, 'converted'), exist_ok=True)
    png_file_exists = False
    progress_window = tk.Toplevel()
    progress_window.title("Conversion Progress")
    icon_data = base64.b64decode(base64_icon)
    icon_image = Image.open(io.BytesIO(icon_data))
    icon_photo = ImageTk.PhotoImage(icon_image)
    progress_window.iconphoto(False, icon_photo)
    progress_window.configure(bg='#242936')
    progress_window.geometry("400x100")
    progress_window.resizable(False, False)
    screen_width = progress_window.winfo_screenwidth()
    screen_height = progress_window.winfo_screenheight()
    x = (screen_width // 2) - (400 // 2)
    y = (screen_height // 2) - (100 // 2)
    progress_window.geometry(f'400x100+{x}+{y}')
    progress_label = tk.Label(progress_window, text="Starting conversion...", bg='#242936', fg='white', anchor='center', font=('Helvetica', 12))
    progress_label.pack(padx=20, pady=(30, 30), fill='x')
    output_type = output_type_var.get()
    all_formats = ['ico', 'png', 'jpeg', 'bmp', 'tiff', 'webp', 'gif', 'pdf', 'svg', 'base64']
    for index, image_file in enumerate(image_files):         
        try:
            if image_file.endswith('.svg'):
                if any(f.endswith('.png') for f in os.listdir(os.path.join(output_folder, 'converted'))):
                    png_file_exists = True
                png_file = os.path.join(output_folder, 'converted', os.path.basename(image_file).replace('.svg', '.png'))
                if not png_file_exists:
                    cairosvg.svg2png(url=image_file, write_to=png_file)
                img = Image.open(png_file).convert('RGBA')
                if output_type == 'all':
                    for fmt in all_formats:
                        final_file_path = os.path.join(output_folder, 'converted', os.path.basename(image_file).replace('.svg', f'.{fmt}'))
                        if fmt == 'jpeg':
                            img.convert('RGB').save(final_file_path, format=fmt.upper())
                        elif fmt == 'svg':
                            convert_to_svg(png_file, img,output_folder)
                        elif fmt == 'base64':
                            convert_to_base64(png_file, output_folder)
                        else:
                            img.save(final_file_path, format=fmt.upper())
                elif output_type == 'base64':
                    convert_to_base64(png_file, output_folder)
                elif output_type == 'svg':
                    convert_to_svg(png_file, img, output_folder)
                else:
                    final_file_path = os.path.join(output_folder, 'converted', os.path.basename(image_file).replace('.svg', f'.{output_type}'))
                    img.save(final_file_path, format=output_type.upper())
                if not png_file_exists and output_type != 'all':
                    os.remove(png_file)
            else:
                img = Image.open(image_file).convert('RGBA')
                if output_type == 'all':
                    for fmt in all_formats:
                        final_file_path = os.path.join(output_folder, 'converted', os.path.basename(image_file).replace(os.path.splitext(image_file)[1], f'.{fmt}'))
                        if fmt == 'jpeg':
                            img.convert('RGB').save(final_file_path, format=fmt.upper())
                        elif fmt == 'svg':
                            convert_to_svg(image_file, img, output_folder)
                        elif fmt == 'base64':
                            convert_to_base64(image_file, output_folder)
                        else:
                            img.save(final_file_path, format=fmt.upper())
                elif output_type != 'base64':
                    final_file_path = os.path.join(output_folder, 'converted', os.path.basename(image_file).replace(os.path.splitext(image_file)[1], f'.{output_type}'))
                    img.save(final_file_path, format=output_type.upper())
            if output_type == 'base64':
                convert_to_base64(image_file, output_folder)
            progress_label.config(text=f'Processing {os.path.basename(image_file)}... ({index + 1}/{len(image_files)})')
            progress_window.update()
        except Exception as e:
            progress_label.config(text=f'Error processing {os.path.basename(image_file)}: {e}')
            progress_window.update()
    progress_label.config(text="Conversion complete!")
    progress_window.update()
    progress_window.after(2000, progress_window.destroy)

def convert_images():
    if selected_image_files: 
        process_images(selected_image_files)

selected_image_files = []
root = TkinterDnD.Tk()
root.title("X2IMG")
root.geometry("250x320")
root.resizable(False, False)
root.configure(bg='#242936')
icon_data = base64.b64decode(base64_icon)
icon_image = Image.open(io.BytesIO(icon_data))
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)
output_title_label = tk.Label(root, text="Output Type:", bg='#242936', fg='white', anchor='center', font=('Helvetica', 12))
output_title_label.pack(pady=(10, 0), fill='x')
frame = tk.Frame(root, bg='#242936')
frame.pack(pady=10)
output_type_var = tk.StringVar(value='ico')
formats = [('ICO', 'ico'), ('PNG', 'png'), ('JPEG', 'jpeg'), ('BMP', 'bmp'), ('TIFF', 'tiff'), ('WEBP', 'webp'), ('GIF', 'gif'), ('PDF', 'pdf'), ('SVG', 'svg'), ('Base64', 'base64'), ('All', 'all')]
for index, (text, value) in enumerate(formats):
    row = index // 3
    column = index % 3
    rb = tk.Radiobutton(frame, text=text, variable=output_type_var, value=value, bg='#242936', fg='white', selectcolor='#242936')
    rb.grid(row=row, column=column, padx=5, pady=5, sticky='w')
selected_files_label = tk.Label(root, text="Selected Files: 0", bg='#242936', fg='white', font=('Helvetica', 10))
selected_files_label.pack(pady=5)
button_frame = tk.Frame(root, bg='#242936')
button_frame.pack(pady=5)
select_files_button = tk.Button(button_frame, text="Select File(s)", command=select_files, bg='gray', fg='white', activebackground='darkgray', relief='flat', bd=0, highlightthickness=0)
select_files_button.pack(side='left', padx=5)
select_folder_button = tk.Button(button_frame, text="Select Folder", command=select_folder, bg='gray', fg='white', activebackground='darkgray', relief='flat', bd=0, highlightthickness=0)
select_folder_button.pack(side='left', padx=5)
convert_button = tk.Button(root, text="Convert", command=convert_images, bg='gray', fg='white', activebackground='darkgray', relief='flat', bd=0, highlightthickness=0)
convert_button.pack(pady=5)
convert_button.config(borderwidth=0, highlightthickness=0, padx=10, pady=5, font=('Helvetica', 10), relief='flat', bg='#3a3f47', activebackground='#4a4f57', fg='white', activeforeground='white')
for button in button_frame.winfo_children(): 
    button.config(borderwidth=0, highlightthickness=0, padx=5, pady=5, font=('Helvetica', 10), relief='flat', bg='#3a3f47', activebackground='#4a4f57', fg='white', activeforeground='white')
root.mainloop()

