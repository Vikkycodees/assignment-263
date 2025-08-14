for i in range(1, 6):             # i goes from 1 to 5
    for j in range(65, 65 + i):  # j goes from ASCII 'A' to 'A' + i - 1
        print(chr(j), end="")    # print letter without space or newline
    print()                      # newline after each row
