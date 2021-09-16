import json
import random

greetings = [
    "Nice to see you today.",
    "Hello, I hope you have a nice day.",
    "Hi there my fellow development resource.",
    "Go away!",
    "Sup dude.",
    "Greetings Earthlings."
]

def handler(event, context):
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': random.choice(greetings) + "\n"
    }