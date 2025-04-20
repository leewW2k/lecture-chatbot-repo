import logging

from dotenv import load_dotenv
from fastapi import APIRouter

from backend.chatservice.chatservice import ChatService
from backend.chatservice.model import ChatRequestBody

load_dotenv()
ROUTE_PREFIX = "/chat"

router = APIRouter(prefix=ROUTE_PREFIX, tags=["chat-service"])


chat_service = ChatService()

@router.post("/{video_id}/v1", status_code=200)
async def get_videos(video_id: str, body: ChatRequestBody):
    retrieval_results, context = chat_service.retrieve_results_prompt(video_id, body.message)
    response = chat_service.generate_video_prompt_response(retrieval_results, body.message, body.previous_messages)
    if response:
        return {"message": "Successfully Retrieve", "answer": response}
    else:
        return {"message": "No Records Found"}

@router.post("/{video_id}", status_code=200)
async def get_videos(video_id: str, body: ChatRequestBody):
    retrieval_results, _ = chat_service.retrieve_results_prompt_clean(video_id, body.message)
    response = chat_service.generate_video_prompt_response(retrieval_results, body.message, body.previous_messages)
    if response:
        return {"message": "Successfully Retrieve", "answer": response}
    else:
        return {"message": "No Records Found"}

@router.post("/testing/{video_id}", status_code=200)
async def get_videos(video_id: str, message: str):
    retrieval_results, context = chat_service.retrieve_results_prompt(video_id, message)
    response = chat_service.generate_video_prompt_response(retrieval_results, message, [])
    if response:
        return {"message": "Successfully Retrieve", "answer": response}
    else:
        return {"message": "No Records Found"}