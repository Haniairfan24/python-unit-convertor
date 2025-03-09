import streamlit as st
import pandas as pd

# Add custom CSS
def apply_custom_css():
    st.markdown("""
        <style>
        /* Main container styling */
        .main {
            padding: 2rem;
            animation: fadeIn 0.8s ease-in;
        }
        
        /* Title styling with animation */
        .title {
            color: #2c3e50;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            text-align: center;
            animation: slideDown 1s ease-out;
        }
        
        /* Subtitle styling with animation */
        .subtitle {
            color: #34495e;
            font-size: 1.2rem;
            text-align: center;
            margin-bottom: 2rem;
            animation: slideDown 1s ease-out 0.2s;
            opacity: 0;
            animation-fill-mode: forwards;
        }
        
        /* Card styling for the converter with hover effect */
        .stButton > button {
            width: 100%;
            background-color: #2980b9;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            font-weight: 500;
            margin-top: 1rem;
            transition: all 0.3s ease;
            transform: scale(1);
        }
        
        .stButton > button:hover {
            background-color: #3498db;
            transform: scale(1.02);
            box-shadow: 0 4px 12px rgba(41, 128, 185, 0.3);
        }
        
        /* Input fields styling with animation */
        .stSelectbox, .stNumberInput {
            margin-bottom: 1rem;
            transition: all 0.3s ease;
            animation: fadeIn 0.8s ease-in;
        }
        
        .stSelectbox:hover, .stNumberInput:hover {
            transform: translateY(-2px);
        }
        
        /* Success message styling with animation */
        .stSuccess {
            background-color: #2ecc71;
            padding: 1rem;
            border-radius: 5px;
            color: white;
            margin-top: 1rem;
            animation: slideUp 0.5s ease-out;
            transition: all 0.3s ease;
        }
        
        /* Error message styling with animation */
        .stError {
            background-color: #e74c3c;
            padding: 1rem;
            border-radius: 5px;
            color: white;
            margin-top: 1rem;
            animation: slideUp 0.5s ease-out;
            transition: all 0.3s ease;
        }
        
        /* Container styling with animation */
        .css-1d391kg {
            padding: 2rem;
            border-radius: 10px;
            background-color: #ffffff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            animation: scaleUp 0.5s ease-out;
            transition: all 0.3s ease;
        }
        
        .css-1d391kg:hover {
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }
        
        /* Columns spacing */
        .css-1r6slb0 {
            gap: 2rem;
        }

        /* Animation keyframes */
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes scaleUp {
            from {
                opacity: 0;
                transform: scale(0.95);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        /* Smooth scrolling */
        * {
            scroll-behavior: smooth;
        }

        /* Pulse animation for the convert button */
        @keyframes pulse {
            0% {
                box-shadow: 0 0 0 0 rgba(41, 128, 185, 0.4);
            }
            70% {
                box-shadow: 0 0 0 10px rgba(41, 128, 185, 0);
            }
            100% {
                box-shadow: 0 0 0 0 rgba(41, 128, 185, 0);
            }
        }

        .stButton > button:active {
            animation: pulse 0.3s ease-out;
        }

        /* Floating animation for select boxes */
        .stSelectbox {
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0% {
                transform: translateY(0px);
            }
            50% {
                transform: translateY(-5px);
            }
            100% {
                transform: translateY(0px);
            }
        }
        </style>
    """, unsafe_allow_html=True)

def length_conversion(value, from_unit, to_unit):
    # Base unit is meters
    length_units = {
        'Kilometer': 1000,
        'Meter': 1,
        'Centimeter': 0.01,
        'Millimeter': 0.001,
        'Mile': 1609.34,
        'Yard': 0.9144,
        'Foot': 0.3048,
        'Inch': 0.0254
    }
    return value * length_units[from_unit] / length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    # Base unit is kilograms
    weight_units = {
        'Kilogram': 1,
        'Gram': 0.001,
        'Milligram': 0.000001,
        'Pound': 0.453592,
        'Ounce': 0.0283495
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

def area_conversion(value, from_unit, to_unit):
    # Base unit is square meters
    area_units = {
        'Square Kilometer': 1000000,
        'Square Meter': 1,
        'Square Mile': 2590000,
        'Square Yard': 0.836127,
        'Square Foot': 0.092903,
        'Square Inch': 0.00064516,
        'Hectare': 10000,
        'Acre': 4046.86
    }
    return value * area_units[from_unit] / area_units[to_unit]

def volume_conversion(value, from_unit, to_unit):
    # Base unit is cubic meters
    volume_units = {
        'Cubic Meter': 1,
        'Liter': 0.001,
        'Milliliter': 0.000001,
        'Gallon': 0.00378541,
        'Quart': 0.000946353,
        'Pint': 0.000473176,
        'Cup': 0.000236588
    }
    return value * volume_units[from_unit] / volume_units[to_unit]

def main():
    st.set_page_config(
        page_title="Universal Unit Converter",
        page_icon="🔄",
        layout="centered"
    )
    
    # Apply custom CSS
    apply_custom_css()
    
    # Title with custom CSS class
    st.markdown('<h1 class="title">📐 Universal Unit Converter</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Convert between different units of measurement</p>', unsafe_allow_html=True)
    
    # Create a dictionary of conversion functions
    conversion_functions = {
        'Length': (length_conversion, ['Kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Mile', 'Yard', 'Foot', 'Inch']),
        'Weight': (weight_conversion, ['Kilogram', 'Gram', 'Milligram', 'Pound', 'Ounce']),
        'Temperature': (temperature_conversion, ['Celsius', 'Fahrenheit', 'Kelvin']),
        'Area': (area_conversion, ['Square Kilometer', 'Square Meter', 'Square Mile', 'Square Yard', 'Square Foot', 'Square Inch', 'Hectare', 'Acre']),
        'Volume': (volume_conversion, ['Cubic Meter', 'Liter', 'Milliliter', 'Gallon', 'Quart', 'Pint', 'Cup'])
    }
    
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        category = st.selectbox("Select Category", list(conversion_functions.keys()))
        value = st.number_input("Enter Value", value=0.0)
    
    with col2:
        conversion_function, units = conversion_functions[category]
        from_unit = st.selectbox("From Unit", units)
        to_unit = st.selectbox("To Unit", units)
    
    if st.button("Convert"):
        try:
            result = conversion_function(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
