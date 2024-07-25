import os.path

FILE_HEAD = """\
[Design]
Version=1.0

"""


def append_document(lib_pkg, folder, document_count):
    for root, dirs, files in os.walk(folder):
        for f in files:
            document_count[0] += 1
            lib_pkg.write("[Document{}]\n".format(document_count[0]))
            lib_pkg.write("DocumentPath={}\n".format(os.path.join(root, f)))
            lib_pkg.write("\n")


def generate_project():
    file_path = os.path.join("QLibrary.LibPkg")
    with open(file_path, "w") as lib_pkg:
        lib_pkg.write(FILE_HEAD)
        document_count = [0]
        append_document(lib_pkg, "Footprint", document_count)
        append_document(lib_pkg, "Symbol", document_count)


if __name__ == "__main__":
    generate_project()
