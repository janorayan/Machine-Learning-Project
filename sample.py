with open("customer_records.txt", "r") as file:
    content = file.read() # The entire file contents -> string object
    print(content)
    print(type(content))
    import re

    with open("customer_records.txt", "r") as file:
    content = file.read() # The entire file contents -> str object
    pattern = r"[6-9]\d{4}\d{4}\s\d{5}"
    extract + re.findall(pattern, content)
    print(extract)
