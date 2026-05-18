from app import Me
m = Me()
print("Initialized!")
try:
    res = m.chat("Hi, what is your name?", [])
    print("Response:", res)
except Exception as e:
    import traceback
    traceback.print_exc()
