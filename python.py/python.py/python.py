with open("demo.log", "r") as file:
    for line in file:
        if "error" in line:
            with open("error.log", "a") as error_file:
                error_file.write(line)
        elif "info" in line:
            with open("info.log", "a") as info_file:
                info_file.write(line)