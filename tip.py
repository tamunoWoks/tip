def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    amount = float(d.replace("$", ""))
    return round(amount, 2)


def percent_to_float(p):
    percentage = float(p.replace("%", ""))
    return percentage / 100


if __name__ == "__main__":
    main()
