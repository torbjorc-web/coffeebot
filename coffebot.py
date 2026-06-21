def coffee_bot():
    print("Welcome to the cafe!")

    size = get_size()
    drink_type = get_drink_type()
    cup = get_cup_type()
    temp = get_temperature()
    extra = order_extra_drink()

    print(f"Alright, that's a {size} {temp} {drink_type} in a {cup} cup!")
    if extra:
        print(f"Also adding a {extra}.")

    name = input("Can I get your name please? ")
    print(f"Thanks, {name}! Your drink will be ready shortly.")


def get_size():
    res = input("What size drink can I get for you? 
[a] Small 
[b] Medium 
[c] Large 
> ")
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()


def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")


def get_drink_type():
    res = input("What type of drink would you like? 
[a] Brewed Coffee 
[b] Mocha 
[c] Latte 
> ")
    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return 'mocha'
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()


def order_latte():
    res = input("And what kind of milk for your latte? 
[a] 2% milk 
[b] Non-fat milk 
[c] Soy milk 
> ")
    if res == 'a':
        return 'latte'
    elif res == 'b':
        return 'non-fat latte'
    elif res == 'c':
        return 'soy latte'
    else:
        print_message()
        return order_latte()


def get_cup_type():
    res = input("Would you like a cup? 
[a] Disposable cup 
[b] Reusable cup 
> ")
    if res == 'a':
        return 'disposable'
    elif res == 'b':
        return 'reusable'
    else:
        print_message()
        return get_cup_type()


def get_temperature():
    res = input("Would you like your drink hot or iced? 
[a] Hot 
[b] Iced 
> ")
    if res == 'a':
        return 'hot'
    elif res == 'b':
        return 'iced'
