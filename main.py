
from Text_Summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Text_Summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

from Text_Summarizer.logging import logger

STAGE_NAME=  "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>>>>> Initialize {STAGE_NAME}  <<<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>>> Completed {STAGE_NAME} Successfully  <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME =  "Data Validaiton Stage"
try:
    logger.info(f">>>>>>>>>>>>> Initialize {STAGE_NAME}  <<<<<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>>>>> Completed {STAGE_NAME} Successfully  <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e





