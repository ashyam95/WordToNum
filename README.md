# Word to Number
This is a slightly modified version of Akshay Nagpal's [w2n](https://github.com/akshaynagpal/w2) package which converts number in words to numeric value. This one is specifically for the **Indian Number System**.
This module converts number in words to numeric value. (eg. eighty four -> 84).
It uses **Indian Number System** (i.e. lakhs and crores).
Below is the installation, usage and other details of this module.

## Installation
### Manual
* Download the **word_to_num.py**
* Paste it in your project location
* Import and use
### Using pip
Please ensure that you have **updated pip** to the latest version before installing word2number.

```
    pip install wordtonum
```

## Usage

Import the module
```
    from WordToNum.word_to_num import WordToNum
```
Instantiate the object
```
    wtn = WordToNum()
```
Then you can use the **to_num** method from this class to convert a string to numeric digits, as shown below.
```
wtn.to_num('two lakhs three thousand nine hundred and eighty four')
203984
```
```
wtn.to_num('one hundred thirty-five'))
135
```
It also supports decimal points
```
wtn.to_num('twenty six point three')
26.3
```
```
wtn.to_num('point one'))
0.1
```
Most of the errors are raised
```
wtn.to_num('three thousand lakh'))
ValueError: Malformed number! Please enter a valid number word (eg. two lakhs twenty three thousand and forty nine)
```
```
wtn.to_num('Some text'))
ValueError: No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)
```
## Bugs/Errors

If you find any bugs/errors in the usage of above code, please raise an issue through [Github](http://github.com/ashyamzubair/WordToNum). If you don't know how to use Github or raise an issue through it, send an email to ashyamzubair@gmail.com with a clear example that can reproduce the issue.

## License
The MIT License (MIT)

Copyright (c) 2016 Akshay Nagpal (https://github.com/akshaynagpal)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
