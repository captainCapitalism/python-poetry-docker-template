import subprocess


def run():
    delete_directory = ["rm", "-r", "python-project"]
    run_cookiecutter = ["cookiecutter", ".", "--no-input"]
    subprocess.run(
        delete_directory
    )
    subprocess.run(run_cookiecutter)

if __name__ == "__main__":
    run()