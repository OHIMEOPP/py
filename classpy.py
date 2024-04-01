with open("作業.txt", "r") as f:
    print(f.read(30))
    f.seek(0)

    lines = f.readlines()
    for i in lines:
        print(i.strip())
