mock_schemas = [
    {
        "formTitle": "Medical Intake Form",
        "formId": "form_001",
        "fields": [
            {
                "id": "field_01",
                "label": "Full Name",
                "type": "text",
                "required": True,
                "value": None,
                "boundingBox": {"x": 100, "y": 200, "width": 300, "height": 30},
                "grouping": {"visualGroup": "Personal Info", "logicalRule": None},
                "accessibility": {
                    "screenReaderHint": "Enter your full legal name",
                    "tabOrder": 1
                }
            },
            {
                "id": "field_02",
                "label": "Date of Birth",
                "type": "date",
                "required": True,
                "value": None,
                "boundingBox": {"x": 100, "y": 250, "width": 200, "height": 30},
                "grouping": {"visualGroup": "Personal Info", "logicalRule": None},
                "accessibility": {
                    "screenReaderHint": "Enter date in MM/DD/YYYY format",
                    "tabOrder": 2
                }
            },
            {
                "id": "field_03",
                "label": "Gender",
                "type": "radio",
                "options": ["Male", "Female", "Other"],
                "required": False,
                "value": None,
                "boundingBox": {"x": 100, "y": 300, "width": 300, "height": 60},
                "grouping": {"visualGroup": "Demographics", "logicalRule": "selectOne"},
                "accessibility": {
                    "screenReaderHint": "Select your gender",
                    "tabOrder": 3
                }
            }
        ]
    },
    {
        "formTitle": "Conference Registration",
        "formId": "form_002",
        "fields": [
            {
                "id": "field_01",
                "label": "Attendee Name",
                "type": "text",
                "required": True,
                "value": None,
                "boundingBox": {"x": 50, "y": 100, "width": 250, "height": 30},
                "grouping": {"visualGroup": "Attendee Info", "logicalRule": None},
                "accessibility": {
                    "screenReaderHint": "Enter your full name as it should appear on your badge",
                    "tabOrder": 1
                }
            },
            {
                "id": "field_02",
                "label": "Email Address",
                "type": "email",
                "required": True,
                "value": None,
                "boundingBox": {"x": 50, "y": 140, "width": 250, "height": 30},
                "grouping": {"visualGroup": "Attendee Info", "logicalRule": None},
                "accessibility": {
                    "screenReaderHint": "Enter a valid email address",
                    "tabOrder": 2
                }
            },
            {
                "id": "field_03",
                "label": "Ticket Type",
                "type": "dropdown",
                "options": ["Standard", "VIP", "Student"],
                "required": True,
                "value": None,
                "boundingBox": {"x": 50, "y": 180, "width": 200, "height": 30},
                "grouping": {"visualGroup": "Ticket Info", "logicalRule": None},
                "accessibility": {
                    "screenReaderHint": "Select your ticket type",
                    "tabOrder": 3
                }
            }
        ]
    },
    {
        "formTitle": "Job Application",
        "formId": "form_003",
        "fields": [
            {
                "id": "field_01",
                "label": "Applicant Name",
                "type": "text",
                "required": True,
                "value": None,
                "boundingBox": {"x": 20, "y": 50, "width": 300, "height": 30},
                "grouping": {"visualGroup": "Personal Details", "logicalRule": None},
                "accessibility": {
                    "screenReaderHint": "Enter your full legal name",
                    "tabOrder": 1
                }
            },
            {
                "id": "field_02",
                "label": "Phone Number",
                "type": "tel",
                "required": True,
                "value": None,
                "boundingBox": {"x": 20, "y": 90, "width": 200, "height": 30},
                "grouping": {"visualGroup": "Personal Details", "logicalRule": None},
                "accessibility": {
                    "screenReaderHint": "Enter your phone number including area code",
                    "tabOrder": 2
                }
            },
            {
                "id": "field_03",
                "label": "Resume",
                "type": "file",
                "required": True,
                "value": None,
                "boundingBox": {"x": 20, "y": 130, "width": 400, "height": 30},
                "grouping": {"visualGroup": "Documents", "logicalRule": None},
                "accessibility": {
                    "screenReaderHint": "Upload your resume in PDF format",
                    "tabOrder": 3
                }
            },
            {
                "id": "field_04",
                "label": "Position Applied For",
                "type": "dropdown",
                "options": ["Engineer", "Designer", "Manager"],
                "required": True,
                "value": None,
                "boundingBox": {"x": 20, "y": 170, "width": 250, "height": 30},
                "grouping": {"visualGroup": "Job Info", "logicalRule": None},
                "accessibility": {
                    "screenReaderHint": "Select the position you are applying for",
                    "tabOrder": 4
                }
            }
        ]
    }
]

# Example: export for use in other files
__all__ = ["mock_schemas"]