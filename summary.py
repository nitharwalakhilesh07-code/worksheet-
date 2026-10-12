with open('mylog.txt', 'r') as file:
    for line in file:
        if "ERROR" in line:
            with open('error_log.txt', 'a') as error_file:
        elif "info" in line:
            with open('info_log.txt', 'a') as f
                f.write(line)
                