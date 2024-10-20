import re

def validate_number_plate(number_plate):
    """
    Validate an Indian number plate for private vehicles.
    
    Parameters:
    number_plate (str): The number plate to validate.
    
    Returns:
    bool: True if the number plate is valid, False otherwise.
    """
    pattern = re.compile(r'^[A-Z]{2} \d{2} [A-Z]{2} \d{4}$')
    
    if pattern.match(number_plate):
        return True
    else:
        return False

def main():
    number_plate = input("Enter the number plate: ")
    
    if validate_number_plate(number_plate):
        print("The number plate is valid.")
    else:
        print("The number plate is not valid.")

if __name__ == "__main__":
    main()