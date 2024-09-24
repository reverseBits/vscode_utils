# vscode_utils
VsCode utils that are useful for initial setup and also the guide on "How to use extensions?"

#### Installation
1. Command to install the vs code extension through cmd

```
 code <extension-id> --install-extension 
 ```

2. Ensure code Command is Available
    -The script uses the code command to interact with VS Code. If the command is not recognized, you may need to add VS Code to your system’s environment variables.

    -To verify or set this up:
        -Open VS Code.
        -Press Ctrl + Shift + P to open the Command Palette.
        -Type Shell Command: Install 'code' command in PATH and select it.
        -This will configure your environment to recognize the code command.

3. To run the .sh file type 

```
bash vscode_installation_script.sh
```

#### Usage of Extensions

1. ##### ms-python.python:
    The official Python extension for Visual Studio Code. It provides features like IntelliSense (code completion), linting, debugging, and support for Jupyter notebooks.

    Usage:- Install the extension and open a Python file to activate features. You can configure linting and formatting settings in your workspace settings.

    [Source](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

2. ##### Codeium.codeium:
    An AI-powered code completion tool that helps you write code faster by suggesting completions based on the context of your code.
    
    A spell checker for your code and text files. It helps catch spelling errors in comments, strings, and documentation.

    Usage:- After installation, it will provide autocomplete suggestions as you type. Customize settings for suggestion frequency and style.

    [Source](https://marketplace.visualstudio.com/items?itemName=Codeium.codeium)
    
    NOTE:- Please Sign-in or Sign-up to use the codeium

3. ##### charliermarsh.ruff:
    An extension that integrates Ruff, a fast linter for Python. It helps identify and fix code style issues quickly.
    
    Usage:- ctrl+s and it will format the code for you remove any unwanted spaces and also reformat the imports

    Install the extension, you can aslo configure it in your settings, and Ruff will run automatically on your Python files to catch linting errors.

    [Source](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

4. ##### KevinRose.vsc-python-indent: 
    This extension enhances Python indentation handling, providing better auto-formatting and maintaining consistent indentation levels in Python files.

    Usage:- Automatically detects whether indent is proper or not

    [Source](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)

5. ##### atommaterial.a-file-icon-vscode:
    This extension adds file icons to your project in the file explorer, helping to visually differentiate file types at a glance.

    Usage:-Just install it, and it will automatically change your file icons based on file type.

    [Source](https://marketplace.visualstudio.com/items?itemName=AtomMaterial.a-file-icon-vscode)

6. ##### streetsidesoftware.code-spell-checker: 
    A spell checker for your code and text files. It helps catch spelling errors in comments, strings, and documentation.

    Usage:-  Install and it will underline misspelled words. Configure the dictionary and ignore settings as needed.

    [Source](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)

7. ##### njpwerner.autodocstring:
    Automatically generates docstrings for Python functions and methods.

    Usage:- Place your cursor on a function and use the command palette or a keyboard shortcut to generate a docstring template.

    [Source](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)

8. ##### ms-azuretools.vscode-docker:
    Provides tools for building, managing, and deploying containerized applications with Docker.

    Usage:-  Install Docker, then use the Docker view in the sidebar to manage images and containers.

    [Source](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

9. ##### ms-vscode-remote.remote-containers:
    Lets you develop inside Docker containers, providing a consistent development environment.

    Usage:- Create a .devcontainer folder in your project, then open the folder in a containerized environment.

    [Source](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

10. ##### eamodio.gitlens:
    Enhances Git capabilities, providing insights into code changes and authorship.

    Usage:- After installation, hover over lines of code to see authorship information and use the GitLens sidebar for additional insights.

    [Source](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

11. ##### Gruntfuggly.todo-tree:
    Scans your project for TODO comments and presents them in a tree view.

    Usage:-  Install it, and it will automatically display a TODO tree in the sidebar. Configure your TODO patterns in settings.

    [Source](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)

12. ##### vsls-contrib.codetour:
    Allows you to create and share code tours for your projects, helping others understand your codebase.

    Usage:- Create a new tour and define steps through the command palette, then share the tour with others.

    [Source](https://marketplace.visualstudio.com/items?itemName=vsls-contrib.codetour)

13. ##### MS-vsliveshare.vsliveshare:
    Enables real-time collaborative editing and debugging sessions with others.

    Usage:- Start a Live Share session, share the link with others, and collaborate in real-time on your code.

    [Source](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)

14. ##### cweijan.vscode-database-client2:
    Provides a database client for querying and managing databases directly from VS Code.

    Usage:- Configure your database connections, and use the database explorer to run queries and manage your database.

    [Source](https://marketplace.visualstudio.com/items?itemName=cweijan.vscode-database-client2)

15. ##### njqdev.vscode-python-typehint:
    Helps add type hints to your Python code, enhancing code readability and type checking.

    Usage:- Use the command palette to add type hints automatically to your functions based on their usage.

    [Source](https://marketplace.visualstudio.com/items?itemName=njqdev.vscode-python-typehint)