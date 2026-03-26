error_count = 0

with open("log.txt", "r") as f:
    for line in f:
        if "error" in line:
            print(line.strip())
            error_count += 1

print("\nTotal Errors:", error_count)
