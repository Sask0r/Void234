def calculate_total(price, quantity, discount):
    if price < 0:
        raise ValueError("Некорректная цена")

    if quantity < 1:
        raise ValueError("Некорректное количество")

    if discount < 0 or discount > 50:
        raise ValueError("Некорректная скидка")

    return price * quantity * (100 - discount) / 100