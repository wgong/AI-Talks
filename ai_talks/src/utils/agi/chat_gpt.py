import logging
from typing import List  # NOQA: UP035
import os

import openai
import streamlit as st


@st.cache_data()
def create_gpt_completion(ai_model: str, messages: List[dict]) -> dict:
    try:
        api_key = os.environ.get("OPENAI_API_KEY","")
        if not api_key:
            api_key = st.secrets.api_credentials.api_key
        if not api_key.startswith("sk-") or len(api_key) < 50:
            raise ValueError(f"Invalid API Key: {api_key}")
        
        openai.api_key = api_key
    except (KeyError, AttributeError):
        st.error(st.session_state.locale.empty_api_handler)
    logging.info(f"{messages=}")
    completion = openai.ChatCompletion.create(
        model=ai_model,
        messages=messages,
        # stream=True,
        # temperature=0.7,
    )
    logging.info(f"{completion=}")
    return completion
