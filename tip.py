def dollars_to_float(d):
    amount = float(d.replace('$', ''))
    return round(amount, 2)