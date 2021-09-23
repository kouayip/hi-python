import json
import re
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]

        if file_path.lower().endswith('.ini'): 
            print ("program start...")

            file_format = file_path.split('.')
            file_name = file_format[0].strip()
            f = open(file_path)   
    
            object = {}
            current_group = ""

            while(True):
                line = f.readline()
                if not line:
                    break

                line_format = line.strip()

                if len(line_format) < 1 or line_format[0] in '#;' :
                    continue

                matched_group = re.match("^\[(.*)]$", line_format)
                is_match = bool(matched_group)

                if is_match:
                    if len(line_format) > 2:
                        current_group = line_format[1:len(line_format) - 1]
                        if not hasattr(object, current_group):
                            object[current_group] = {}
                    else:
                        current_group = ""
                else:
                    matched_content = re.match("^(.*)(=)(.*)$", line_format)
                    is_match = bool(matched_content)

                    if is_match and len(current_group) > 0:
                        groups = matched_content.groups()

                        key = groups[0].strip()
                        value = groups[2].strip()
                        
                        object[current_group][key] = value

            f.close()

            print ("processing completed")
            print ("write to the new file")
            # Write file content to json
            new_file_name = file_name.split('.')[0].strip() + ".json"
            with open(new_file_name, 'w') as outfile:
                json.dump(object, outfile)

            print ("final process, the conversion was completed")
        else: 
            print ("*error* file type error")
    else: 
        print ("*error* the program needs a file as an argument")