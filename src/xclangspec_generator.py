# Run with python3
# Script that generates the Logos xclangspec
# 
# xclangspec_generator is a script created by pr0crustes (https://github.com/pr0crustes)
# that is provided as it is, without any warranty.
# pr0crustes - 2018 - all rights reserved.
#

new_keywords = [
    "// Start Logos Keywords",
    "%group",
    "%hook",
    "%new",
    "%subclass",
    "%property",
    "%end",
    "%config",
    "%hookf",
    "%ctor",
    "%dtor",
    "%init",
    "%class",
    "%c",
    "%orig",
    "%log",
    "// End Logos Keywords",
    "// Start Other Keywords",
    "NSLog",
    "NSString",
    "NSInteger",
    "NSObject",
    "// End Other Keywords"
]

print("Reading File...")
objc_spec_file = "/Applications/Xcode.app/Contents/SharedFrameworks/DVTFoundation.framework/Versions/A/Resources/ObjectiveC.xclangspec"
objc_spec_content = []
for line in open(objc_spec_file, 'r'):
    if line.strip():
        if not (line.strip().startswith("/")):
            objc_spec_content.append(line)

print("Parsing File...")
new_lines = []
for i in range(len(objc_spec_content)):
    line = objc_spec_content[i].replace("objc", "logos")
    new_lines.append(line)

    if "Words = (" in line:
        if i > 3:
            if "Chars = \"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_\";" in objc_spec_content[i-1]:
                if "StartChars = \"@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_\";" in objc_spec_content[i-2]:
                    print("Inserting Logos Keywords Into New File...")
                    for new_word in new_keywords:
                        if new_word.strip().startswith("//"):
                            new_lines.append("\t\t\t\t" + new_word + "\n")
                        else:
                            new_lines.append("\t\t\t\t\"" + new_word + "\",\n")

print("Saving New File...")
with open("Logos.xclangspec", "w") as file:
    file.write("// Logos xclangspec was generated by spec_gen\n")
    file.write("// Script made by pr0crustes\n")
    for line in new_lines:
        file.write(line)

print("XClangSpec Generator was successfully runned.")
