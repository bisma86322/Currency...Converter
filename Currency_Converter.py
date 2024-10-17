import streamlit as st

def convert_currency(amount, from_currency, to_currency):
    # Define conversion rates
    rates = {
        'USD': {'PKR': 220.0, 'GBP': 0.75, 'INR': 82.0, 'SAR': 3.75, 'AED': 3.67},
        'PKR': {'USD': 1 / 220.0, 'GBP': 0.0034, 'INR': 0.37, 'SAR': 0.017, 'AED': 0.017},
        'GBP': {'USD': 1.33, 'PKR': 294.0, 'INR': 109.0, 'SAR': 5.00, 'AED': 4.90},
        'INR': {'USD': 0.012, 'PKR': 2.70, 'GBP': 0.0091, 'SAR': 0.046, 'AED': 0.045},
        'SAR': {'USD': 0.27, 'PKR': 58.0, 'GBP': 0.20, 'INR': 21.7, 'AED': 0.98},
        'AED': {'USD': 0.27, 'PKR': 58.0, 'GBP': 0.20, 'INR': 21.7, 'SAR': 1.02},
    }
    
    # Convert amount
    converted_amount = amount * rates[from_currency][to_currency]
    return converted_amount

def format_number(value, currency):
    """Formats the number into appropriate units based on currency."""
    if currency in ['USD', 'GBP', 'INR', 'SAR', 'AED']:
        if value >= 1_000_000_000:
            return f"{value / 1_000_000_000:.2f} B"
        elif value >= 1_000_000:
            return f"{value / 1_000_000:.2f} M"
        else:
            return f"{value:.2f} {currency}"
    elif currency == 'PKR':
        if value >= 1_00_00_000:
            return f"{value / 1_00_00_000:.2f} Crore"
        elif value >= 1_00_000:
            return f"{value / 1_00_000:.2f} Lakh"
        else:
            return f"{value:.2f} {currency}"
    elif currency == 'INR':
        if value >= 1_00_00_000:
            return f"{value / 1_00_00_000:.2f} Crore"
        elif value >= 1_00_000:
            return f"{value / 1_00_000:.2f} Lakh"
        else:
            return f"{value:.2f} {currency}"
    else:
        return str(value)

# Streamlit App
st.title("Currency Converter")

# User input for currency selection
currency_options = {
    '1': 'USD',
    '2': 'PKR',
    '3': 'GBP',
    '4': 'INR',
    '5': 'SAR',
    '6': 'AED'
}

# Select base currency
currency_selection = st.selectbox("Select the base currency:", options=list(currency_options.values()))
from_currency = currency_selection

# Select target currency
target_currency_selection = st.selectbox("Select the target currency:", options=list(currency_options.values()))
to_currency = target_currency_selection

# Input for amount
amount = st.number_input("Enter the amount you want to convert:", min_value=0.0)

# Conversion button
if st.button("Convert"):
    if from_currency != to_currency:
        converted_value = convert_currency(amount, from_currency, to_currency)
        formatted_value = format_number(converted_value, to_currency)
        st.success(f"{amount} {from_currency} is equal to {formatted_value} {to_currency}")
    else:
        st.error("Please select different currencies for conversion.")

