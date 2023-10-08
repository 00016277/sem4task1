def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)

n = int(input("Enter a number: "))

if n > 0:
    print("countdown (" + str(n) + ")")
    print(countdown(n))
else:
    print("countup (" + str(n) + ")")
    print(countup(n))