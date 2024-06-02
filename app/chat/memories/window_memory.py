from langchain.memory import ConversationBufferWindowMemory
from app.chat.memories.histories.sql_history import SqlMessageHistory
from app.chat.models import ChatArgs

def window_buffer_memory_builder(chat_args: ChatArgs):
  return ConversationBufferWindowMemory(
    memory_key="chat_history",
    output_key="answer",
    return_messages=True,
    chat_memory=SqlMessageHistory(
      conversation_id=chat_args.conversation_id,
    ),
    k=2
  )