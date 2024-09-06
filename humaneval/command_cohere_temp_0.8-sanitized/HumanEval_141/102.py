def file_name_check(file_name):
    checker = [{
        "Or": [
            {"And": [
                {"Not": [
                    {"IsInstance": [(str), {"element": file_name, "value": "^\d\d\d$"}]}
                ]},
                {"IsInstance": [(str), {"element": file_name, "value": "^[a-zA-Z][a-zA-Z0-9]*$"}]}
            ]},
            {"And": [
                {"IsInstance": [(str), {"element": file_name, "value": "\."}]}
            ]},
            {"And": [
                {"IsInstance": [(str), {"element": file_name, "value": "txt$"}]}
            ]},
            {"And": [
                {"IsInstance": [(str), {"element": file_name, "value": "exe$"}]}
            ]},
            {"And": [
                {"IsInstance": [(str), {"element": file_name, "value": "dll$"}]}
            ]}
        ]
    }]
    if checker:
        return "Yes"
    else:
        return "No"