from django import template


register = template.Library()
#code to calculate the subtotal
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity