def main():

    n = int(input("Enter the height of the pyramid: "))
    for i in range(1, n + 1):
        spaces = n - i
        hashes = 2 * i - 1
        print(' ' * spaces + '#' * hashes)

if __name__ == "__main__":
    main()
    print()
    input("Press any button to exit")