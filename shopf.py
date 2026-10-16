def calculate_total(price, quantity, discount):
    if price <= 0:
        raise ValueError("Некорректная цена")

    if quantity < 0:
        raise ValueError("Некорректное количество")

    if discount < 0 or discount > 100:
        raise ValueError("Некорректная скидка")

    return price * quantity - discount