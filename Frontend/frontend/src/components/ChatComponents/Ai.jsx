import { usePostAiTextMutation } from '../../app/redux-features/api.js';
import React, { useState } from 'react'
import MessageFormUI from './MessageFormUI'

const Ai = ({props, activeChat}) => {

    const [message, setMessage] = useState("");
    const [attachment, setAttachment] = useState("");
    const [trigger] = usePostAiTextMutation();

    const handleChange = (e) => setMessage(e.target.value)
    const handleSubmit = async () => {
        if (message || attachment !== "") {

            const date = new Date()
            .toISOString()
            .replace("T", " ")
            .replace("Z", `${Math.floor(Math.random() * 1000)}+00:00`);
            
            const at = attachment ? [{blob: attachment, file: attachment.name}]: [];
            const form = {
                attachments: at,
                created: date,
                sender_username: props.username,
                text: message,
                activeChatId: activeChat.id,
            }

            props.onSubmit(form);
            trigger(form);
            setMessage("")
            setAttachment("")
        }
}

const handleKeyDown = () => {

    handleSubmit();

}


  return (
    <MessageFormUI setAttachment={setAttachment} message={message} handleChange={handleChange} handleKeyDown={handleKeyDown} handleSubmit={handleSubmit}/>
  )
}

export default Ai