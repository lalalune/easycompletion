from language import parse_arguments, openai_function_call, openai_text_call, compose_prompt

test_text = "Write a song about AI"
test_function = {
    "name": "write_song",
    "description": "Write a song about AI",
    "parameters": {
        "type": "object",
        "properties": {
            "lyrics": {
                "type": "string",
                "description": "The lyrics for the song",
            }
        },
        "required": ["lyrics"],
    },
}

# TESTS
# Test parse_arguments
test_input = '{"key1": "value1", "key2": 2}'
expected_output = {"key1": "value1", "key2": 2}
assert parse_arguments(test_input) == expected_output, "Test parse_arguments failed"

test_prompt = "I am a {{object}}"
test_dict = {"object": "towel"}

prompt = compose_prompt(test_prompt, test_dict)

assert prompt == "I am a towel", "Test compose_prompt failed"

response = openai_function_call(
    text=test_text, functions=test_function, function_call="write_song"
)
print("Sent message: Write a song about AI")
print("Received response:")
print(response)
print("lyrics")
print(response["arguments"]["lyrics"])

response = openai_text_call("Hello, how are you?")
print("Sent message: Hello, how are you?")
print("Received response:")
print(response)