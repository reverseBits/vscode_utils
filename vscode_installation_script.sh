#!/bin/bash

extensions=(
    'ms-python.python'
    'Codeium.codeium'
    'charliermarsh.ruff'
    'KevinRose.vsc-python-indent'
    'amazonwebservices.amazon-q-vscode'
    'AmazonWebServices.aws-toolkit-vscode'
    'atommaterial.a-file-icon-vscode'
    'streetsidesoftware.code-spell-checker'
    'njpwerner.autodocstring'
    'ms-azuretools.vscode-docker'
    'eamodio.gitlens'
    'Gruntfuggly.todo-tree'
    'vsls-contrib.codetour'
    'coder.coder-remote'
    'MS-vsliveshare.vsliveshare'
    'cweijan.vscode-database-client2'
    'ms-vscode-remote.remote-containers'
    'njqdev.vscode-python-typehint'
)

for extension in "${extensions[@]}"; do
    echo "Installing $extension..."
    code --install-extension "$extension"
done

echo "All extensions installed!"
