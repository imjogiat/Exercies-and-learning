# filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# for filename in filenames:
#     make_file = open(f"{filename}",'x')
#     make_file.close()
#     write_file = open(f"{filename}",'w')
#     write_file.write("Hello")
#     write_file.close()

user_entries = ['10', '19.1', '20']
total = 0.0

[float(user_entry) for user_entry in user_entries]

for user_entry in user_entries:
    total += user_entry

print(total)