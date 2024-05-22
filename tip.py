def dollars_to_float(d):
    amount = float(d.replace('$', ''))
    return round(amount, 2)

def percent_to_float(p):
    percentage = float(p.replace('%', ''))
    return percentage/100