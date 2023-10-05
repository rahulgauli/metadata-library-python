from pydantic import BaseModel

class Programming(BaseModel):
    process_name: str 
    process_inputs: {str:[]}
    process_output: {str:[]}
    process_logs: {str:[]}



