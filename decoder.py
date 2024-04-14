def decode(num):

    decoded = ""

    for char in num:
        if char == "0":
            decoded += "7"

        elif char == "1":
            decoded += "8"

        elif char == "2":
            decoded += "9"

        elif char == "3":
            decoded += "0"

        elif char == "4":
            decoded += "1"

        elif char == "5":
            decoded += "2"

        elif char == "6":
            decoded += "3"

        elif char == "7":
            decoded += "4"

        elif char == "8":
            decoded += "5"

        elif char == "9":
            decoded += "6"

    return decoded