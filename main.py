import time

print("Started Program\n")

while True:
    try:
        num = int(input("How many times would you like to count? (def: 1000000000): "))
    except Exception as e:
        num = 1000000000
    print("\nStarted Counting ({})\n".format(num))
    count = 0
    start = time.perf_counter()
    while count < num:
        count += 1

    print("Finished in: {}".format(time.perf_counter() - start) + " seconds.\n")

    again = input("Would you like to try again? (y/n)")

    if again == "n":
        break
    else:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
