#!/bin/bash

# Membuat direktori config jika belum ada
mkdir -p ~/.termux

# Membuat/mengedit file termux.properties
cat > ~/.termux/termux.properties << EOF
# Key bindings configuration
extra-keys = [ \
['cd wingo && python main.py','ls','/','cd mz && python main.py','UP','python main.py'], \
['TAB','CTRL','ALT','LEFT','DOWN','RIGHT'] \
]

# Contoh kombinasi tombol volume untuk kontrol media
volume-keys = media
EOF

# Reload konfigurasi Termux
termux-reload-settings

echo "Key bindings berhasil diatur!"
