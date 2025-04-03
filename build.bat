@echo off

REM Compile the Python script with Nuitka 
nuitka --standalone --onefile ^
    --windows-console-mode=disable ^
    --include-data-file="dlls\libbz2-1.dll=dlls\libbz2-1.dll" ^
    --include-data-file="dlls\libcairo-2.dll=dlls\libcairo-2.dll" ^
    --include-data-file="dlls\libexpat-1.dll=dlls\libexpat-1.dll" ^
    --include-data-file="dlls\libfontconfig-1.dll=dlls\libfontconfig-1.dll" ^
    --include-data-file="dlls\libfreetype-6.dll=dlls\libfreetype-6.dll" ^
    --include-data-file="dlls\libgcc_s_seh-1.dll=dlls\libgcc_s_seh-1.dll" ^
    --include-data-file="dlls\libglib-2.0-0.dll=dlls\libglib-2.0-0.dll" ^
    --include-data-file="dlls\libgraphite2.dll=dlls\libgraphite2.dll" ^
    --include-data-file="dlls\libharfbuzz-0.dll=dlls\libharfbuzz-0.dll" ^
    --include-data-file="dlls\libiconv-2.dll=dlls\libiconv-2.dll" ^
    --include-data-file="dlls\libintl-8.dll=dlls\libintl-8.dll" ^
    --include-data-file="dlls\libpcre-1.dll=dlls\libpcre-1.dll" ^
    --include-data-file="dlls\libpixman-1-0.dll=dlls\libpixman-1-0.dll" ^
    --include-data-file="dlls\libpng16-16.dll=dlls\libpng16-16.dll" ^
    --include-data-file="dlls\libstdc++-6.dll=dlls\libstdc++-6.dll" ^
    --include-data-file="dlls\libwinpthread-1.dll=dlls\libwinpthread-1.dll" ^
    --include-data-file="dlls\zlib1.dll=dlls\zlib1.dll" ^
    --windows-icon-from-ico=X2IMG.ico ^
    --enable-plugin=tk-inter ^
    --include-package=cairosvg ^
    X2IMG.py

REM Pause to see the output
pause
