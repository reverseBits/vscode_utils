import subprocess
import platform

os_type = platform.system()

def find_code_path():
    if os_type == "Windows":
        code_path = subprocess.run(["where", "code.cmd"], capture_output=True, text=True).stdout.strip()
    else:
        code_path = subprocess.run(["which", "code"], capture_output=True, text=True).stdout.strip()

    if not code_path:
        raise FileNotFoundError("VS Code 'code' command not found in PATH")

    return code_path

code_path = find_code_path()

extensions = [
    'ms-python.python',
    'Codeium.codeium',
    'charliermarsh.ruff',
    'KevinRose.vsc-python-indent',
    'amazonwebservices.amazon-q-vscode',
    'AmazonWebServices.aws-toolkit-vscode',
    'atommaterial.a-file-icon-vscode',
    'streetsidesoftware.code-spell-checker',
    'njpwerner.autodocstring',
    'ms-azuretools.vscode-docker',
    'eamodio.gitlens',
    'Gruntfuggly.todo-tree',
    'vsls-contrib.codetour',
    'coder.coder-remote',
    'MS-vsliveshare.vsliveshare',
    'cweijan.vscode-database-client2',
    'ms-vscode-remote.remote-containers',
    'njqdev.vscode-python-typehint'
    
]

def get_installed_extensions():
    result = subprocess.run([code_path, '--list-extensions'], capture_output=True, text=True)
    if result.returncode == 0:
        installed_extensions = set(result.stdout.split())
        return installed_extensions
    else:
        print("Failed to retrieve installed extensions")
        print(result.stderr)
        return set()

installed_extensions = get_installed_extensions()

def install_extension(extension_id):
    if extension_id in installed_extensions:
        print(f"Extension {extension_id} is already installed.")
        return

    print(f"Installing {extension_id}...")
    result = subprocess.run([code_path, '--install-extension', extension_id], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Successfully installed {extension_id}")
        installed_extensions.add(extension_id)
    else:
        print(f"Failed to install {extension_id}")
        print(result.stderr)

for ext in extensions:
    install_extension(ext)
