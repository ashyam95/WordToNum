# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 18:59:35 2018

@author: azubair
"""
class WordToNum(object):
    def __init__(self):
        self.decimal_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        
        self.indian_number_system = {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'eleven': 11,
            'twelve': 12,
            'thirteen': 13,
            'fourteen': 14,
            'fifteen': 15,
            'sixteen': 16,
            'seventeen': 17,
            'eighteen': 18,
            'nineteen': 19,
            'twenty': 20,
            'thirty': 30,
            'forty': 40,
            'fifty': 50,
            'sixty': 60,
            'seventy': 70,
            'eighty': 80,
            'ninety': 90,
            'hundred': 100,
            'thousand': 1000,
            'grand': 1000,
            'lacs': 100000,
            'lakhs': 100000,
            'lac': 100000,
            'lakh': 100000,
            'crore': 10000000,
            'crores': 10000000,
            'point': '.'
        }


    def number_formation(self, number_words):
        """
        Form numeric multipliers for lakhs, crores, thousand etc.
        
        Parameters:
        number_words (list): List of strings

        Returns
        int
        """
        numbers = []
        for number_word in number_words:
            numbers.append(self.indian_number_system[number_word])
            
        if len(numbers) == 4:
            return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
        elif len(numbers) == 3:
            return numbers[0] * numbers[1] + numbers[2]
        elif len(numbers) == 2:
            if 100 in numbers:
                return numbers[0] * numbers[1]
            else:
                return numbers[0] + numbers[1]
        else:
            return numbers[0]

    def get_decimal_sum(self, decimal_digit_words):    
        """
        Convert post decimal digit words to numerial digits
        
        Parameters:
        decimal_digit_words (list): List of strings
        
        Returns:
        float
        """
        decimal_number_str = []
        for dec_word in decimal_digit_words:
            if(dec_word not in self.decimal_words):
                return 0
            else:
                decimal_number_str.append(self.indian_number_system[dec_word])
        final_decimal_string = '0.' + ''.join(map(str,decimal_number_str))
        return float(final_decimal_string)

    def to_num(self, number_sentence):
        """
        Convert string representation of number to an actual number
        
        Parameters:
        number_sentence (str): Number in words
        
        Returns:
        int/float/None: The number in integer/float type
        """
        # Raise error if input is not a string
        if type(number_sentence) is not str:
            raise ValueError("Type of input is not string! Please enter a valid number word (eg. two lakhs twenty three thousand and forty nine)")
    
        number_sentence = number_sentence.replace('-', ' ')
        number_sentence = number_sentence.lower()  # Converting input to lowercase
    
        # Return th enumber if the number is entered as string (eg: '24')
        if(number_sentence.isdigit()):
            return int(number_sentence)
    
        split_words = number_sentence.strip().split()  # strip extra spaces and split sentence into words
    
        clean_numbers = []
        clean_decimal_numbers = []
    
        # Removing and, & etc.
        for word in split_words:
            if word in self.indian_number_system:
                clean_numbers.append(word)
    
        # Raise error message if the user enters invalid input!
        if len(clean_numbers) == 0:
            raise ValueError("No valid number words found! Please enter a valid number word (eg. two lakhs twenty three thousand and forty nine)") 
    
        # Raise rror if user enters million, billion, thousand or decimal point twice
        if clean_numbers.count('thousand') > 1 or clean_numbers.count('lakh') > 1 or clean_numbers.count('crore') > 1 or clean_numbers.count('point')> 1:
            raise ValueError("Redundant number word! Please enter a valid number word (eg. two lakhs twenty three thousand and forty nine)")
    
        # Separate the decimal part of number (if exists)
        if clean_numbers.count('point') == 1:
            clean_decimal_numbers = clean_numbers[clean_numbers.index('point')+1:]
            clean_numbers = clean_numbers[:clean_numbers.index('point')]
            
        # Get the index of crores/lakhs/thousands
        crore_index = -1
        lakh_index = -1
        thousand_index = -1
        
        for number in clean_numbers:
            crore_terms = ['crore', 'crores']
            lakh_terms = ['lac', 'lacs', 'lakh', 'lakhs']
            thousand_terms = ['thousand', 'grand']
    
            if number in crore_terms:
                crore_index = clean_numbers.index(number)
            elif number in lakh_terms:
                lakh_index = clean_numbers.index(number)
            elif number in thousand_terms:
                thousand_index = clean_numbers.index(number)
                
        # Raise error if thousand comes before lakhs/crores or lakhs comes before crore
        if (thousand_index > -1 and (thousand_index < lakh_index or thousand_index < crore_index)) or (lakh_index>-1 and lakh_index < crore_index):
            raise ValueError("Malformed number! Please enter a valid number word (eg. two lakhs twenty three thousand and forty nine)")
    
        total_sum = 0  # storing the number to be returned
    
        if len(clean_numbers) > 0:
            # hack for now, better way TODO
            if len(clean_numbers) == 1:
                    total_sum += self.indian_number_system[clean_numbers[0]]
    
            else:
                if crore_index > -1:
                    crore_multiplier = self.number_formation(clean_numbers[0:crore_index])
                    total_sum += crore_multiplier * 10000000
    
                if lakh_index > -1:
                    if crore_index > -1:
                        lakh_multiplier = self.number_formation(clean_numbers[crore_index+1:lakh_index])
                    else:
                        lakh_multiplier = self.number_formation(clean_numbers[:lakh_index])
                    total_sum += lakh_multiplier * 100000
    
                if thousand_index > -1:
                    if lakh_index > -1:
                        thousand_multiplier = self.number_formation(clean_numbers[lakh_index+1:thousand_index])
                    elif crore_index > -1 and lakh_index == -1:
                        thousand_multiplier = self.number_formation(clean_numbers[crore_index+1:thousand_index])
                    else:
                        thousand_multiplier = self.number_formation(clean_numbers[:thousand_index])
                    total_sum += thousand_multiplier * 1000
    
                if thousand_index > -1 and thousand_index != len(clean_numbers)-1:
                    hundreds = self.number_formation(clean_numbers[thousand_index+1:])
                elif lakh_index > -1 and lakh_index != len(clean_numbers)-1:
                    hundreds = self.number_formation(clean_numbers[lakh_index+1:])
                elif crore_index > -1 and crore_index != len(clean_numbers)-1:
                    hundreds = self.number_formation(clean_numbers[crore_index+1:])
                elif thousand_index == -1 and lakh_index == -1 and crore_index == -1:
                    hundreds = self.number_formation(clean_numbers)
                else:
                    hundreds = 0
                total_sum += hundreds
    
            # Ading decimal part to total_sum (if exists)
            decimal_sum = self.get_decimal_sum(clean_decimal_numbers)
            if decimal_sum:
                total_sum += decimal_sum
    
        return total_sum