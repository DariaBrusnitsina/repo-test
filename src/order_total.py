"""Very small demo module for a documentation repository."""


def calculate_order_total(price: float, quantity: int, delivery_fee: float = 0.0) -> float:
    """Return the total order amount."""
    return round(price * quantity + delivery_fee, 2)


def has_free_delivery(total: float) -> bool:
    """Free delivery starts from 3000."""
    return total >= 3000


if __name__ == "__main__":
    total = calculate_order_total(price=799.0, quantity=3, delivery_fee=250.0)
    print(f"Order total: {total}")
    print(f"Free delivery: {has_free_delivery(total)}")
