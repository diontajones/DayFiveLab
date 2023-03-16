def apt_search1(city, max_rent, min_beds, pets_allowed=True):
    if pets_allowed:
        return (f'Welcome to GC Property Management! Looking up listings in in {city} for {min_beds} bedroom apartments'
                f'that allow pets, all within a budget of ${max_rent} per month')
    else:
        return (f'Welcome to GC Property Management! Looking up listings in in {city} for {min_beds} bedroom apartments'
                f', all within a budget of ${max_rent} per month')


def apt_search2(city, max_rent, min_beds=1, pets_allowed=True):
    if pets_allowed:
        return (f'Welcome to GC Property Management! Looking up listings in in {city} for {min_beds} bedroom apartments'
                f' that allow pets, all within a budget of ${max_rent} per month')
    else:
        return (f'Welcome to GC Property Management! Looking up listings in in {city} for {min_beds} bedroom apartments'
                f', all within a budget of ${max_rent} per month')


print(apt_search2("Atlanta", 2000))
print(apt_search2("Detroit", 1500, 2))
print(apt_search2(city="Seattle", max_rent=2500, pets_allowed=False))


plus_one_hundred = lambda a: a + 100
print(plus_one_hundred(30))
square_num = lambda b: b ** 2
print(square_num(4))
concatenate = lambda c: "- " + c
print(concatenate('hello'))
divide_by_three = lambda d: d / 3
print(divide_by_three(9))

