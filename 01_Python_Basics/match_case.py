color = input("Enter color: ")

match color:
    case "Green":
        print("GO")
    case "Yellow":
        print("LOOK")
    case "Red":
        print("STOP")
    case _:
        print("wrong color")


