
def work(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        i = 0
        ans = []
        for line in lines:
            if i % 2 == 0:
                ans.append(line)
            i += 1
    return ans

if __name__ == "__main__":
    filename = "100Things/data.txt"  # change to your file name
    lines = work(filename)
    print(lines)
