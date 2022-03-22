def string_list_to_list(string):
    # string = string[1:-1]
    string = string.replace(" ", "")
    string = string.split(",")

    list_data = []
    for s in string:
        list_data.append(float(s))

    return list_data


def list_to_dbarray(list):
    converted_list = [str(element) for element in list]
    dbarray = ",".join(converted_list)
    dbarray = "'{" + dbarray + "}'"
    # print(dbarray)
    return dbarray
