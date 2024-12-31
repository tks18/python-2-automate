# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Tools\\Automation Scripts\\python-2automate'],
             binaries=[],
             datas=[('images/logo.png', 'automate-logo'), ('images/logo.ico', 'automate-logo'), ('fonts/Roboto-Bold.ttf', 'automate-fonts'), ('fonts/Roboto-Regular.ttf', 'automate-fonts')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Python 2 Automate',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          version='version.txt',
          icon='C:\\Tools\\Automation Scripts\\python-2automate\\images\\logo.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
