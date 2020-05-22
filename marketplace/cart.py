from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from marketplace.db import get_db
from marketplace.auth import login_required

bp = Blueprint('cart', __name__)

@bp.route('/add_cart/<int:item_id>', methods=['POST'])
@login_required
def add_cart(item_id):
    db = get_db()
    # TODO: Add Item to the user's cart
    flash("Item successfully added to cart", 'success')
    return redirect(url_for('store.index'))

@bp.route('/checkout', methods=['GET'])
@login_required
def checkout():
    db = get_db()
    # TODO: Select all of the items in a user's cart and the total price of all the items
    return render_template('cart/checkout.html', cart_items=cart_items, total_price=total_price)


@bp.route('/delete/<cart_item_id>', methods=['POST'])
@login_required
def delete_item(cart_item_id):
    # TODO: Delete an item from your cart
    return redirect(url_for('cart.checkout'))
