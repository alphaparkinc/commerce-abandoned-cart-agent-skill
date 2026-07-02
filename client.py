import os
from typing import Dict, Any

class AbandonedCartRecoveryClient:
    def process_recovery(self, customer_email: str, cart_items: list, inactivity_hours: int) -> Dict[str, Any]:
        cart_value = sum(item.get("price", 0.0) * item.get("quantity", 1) for item in cart_items)
        discount = 0.0
        coupon = ""
        if cart_value > 150.0:
            discount = 15.0
            coupon = "COMEBACK15"
        elif cart_value > 50.0:
            discount = 10.0
            coupon = "COMEBACK10"
            
        email_body = f"Hi, we noticed you left items in your cart. Use {coupon} for {discount}% off."
        return {
            "cart_value": cart_value,
            "discount_percentage": discount,
            "recovery_coupon": coupon,
            "recovery_email_draft": email_body,
            "trigger_follow_up": inactivity_hours >= 24
        }
