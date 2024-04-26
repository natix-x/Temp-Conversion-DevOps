FROM tensorflow/serving

ENV MODEL_NAME tensorflow_model

COPY tensorflow_model /models/${MODEL_NAME}

EXPOSE 8501

CMD tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=${MODEL_NAME} --model_base_path=/models/${MODEL_NAME}
