"""
Author: David Rodriguez Perez
File: main.py
Description: Runs main functions in interface between instrument signal and app message.
             If lab instrument fails, it sends a signal which is then translated into some
             input by the Raspberry pi which then throws that input at the program. This 
             input is picked up by detect_signal(), which then returns True (False if
             nothing is picked up). This then calls send_message(signal), which depending
             on boolean signal, lets the user know if the lab intrument ran into a problem
             or ran succesfully (no signal sent).
Date: 12/7/2016
"""

def main():
    signal = detect_signal()
    send_message(signal)

def detect_signal():
    inp = raw_input("Enter input: ")
    if(inp != ""):
        return True
    return False

def send_message(signal):
    if(signal):
        print("ERROR SIGNAL PICKED UP")
    else:
        print("SUCCESS")

main()