import base64

message = "I love you"
message_in_bytes =bytes(message,"utf-8")
encoded_message = base64.b64encode(message_in_bytes)

message2 = "SSBsb3ZlIHlvdQ=="
message2_in_bytes = bytes(message2,"utf-8")
decoded_message = base64.b64decode(message2_in_bytes)

print(f"Encoded:{encoded_message} Decoded:{decoded_message}")
