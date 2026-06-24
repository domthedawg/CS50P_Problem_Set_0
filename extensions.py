import os

file_type = input("File name: ")

name, extension = os.path.splitext(file_type)

extension = extension.lower().lstrip(".")

match extension:
    case "png" | "jpeg" | "jpg" | "gif":
        print(f"image/{extension}")
    case "pdf":
        print(f"application/{extension}")
    case "txt":
        print(f"document/{extension}")
    case "zip":
        print(f"folder/{extension}")
    case _:
        print("application/octet-stream")