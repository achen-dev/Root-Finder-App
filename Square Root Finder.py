# This is a simple square root finder using text prompts


def non_natural_root(target, guess):
    """This function will try to narrow down a non whole root number by using the average of the target and the guess"""
    if abs((guess * guess) - target) < 0.001:
        print(guess)
    else:
        lower_bound = target / guess
        new_guess = (guess + lower_bound) / 2
        non_natural_root(target, new_guess)


def find_root(target):
    """This function will find the square root of a given target number using iterated estimation"""
    target = int(target)
    for i in range(0, 9999999999):
        if i*i == target:
            print(i)
            break
        elif abs((i*i)-target) < 0.001:
            print(i)
            break
        elif i*i > target:
            non_natural_root(target, i)
            break


if __name__ == "__main__":
    print("Welcome to Alan's square root finder app")
    while True:
        target = input("Please input the number you wish to find the root of: (insert blank to exit app)")
        if target == "":
            print("Thank You!")
            break
        else:
            try:
                target = float(target)
                print("Here is your result:")
                find_root(target)

            except:
                print("Please input a number")







