from fastapi import APIRouter, File, UploadFile
from src.candidate import service

router = APIRouter()


@router.post("/analyse")
async def analyse_candidate(file: UploadFile = File(...)):    

    file_name = await service.save_cv_candidate(file=file)

    cv_content = service.read_cv_candidate(file_name=file_name)

    result = service.analyse_candidate(cv_content=cv_content)

    return result
