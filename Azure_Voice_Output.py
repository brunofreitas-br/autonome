import azure.cognitiveservices.speech as speechsdk
#from Place_Helper import Place_text



#Dados de autenticação da API
speech_key, service_region = "c75e5de2120e4489971c921491c84913", "eastus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_config.speech_synthesis_language = "pt-BR"




#Função de Output do Azure (Text-to-Voice)
def Azure_Output():

    # Creates a speech synthesizer using the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)


    #Recebe a Localização do Place_Helper
    from faces import phrase
    text = phrase
    #name = person_name_text


    # Sintetiza o texto da função para audio
    # The synthesized speech is expected to be heard on the speaker with this line executed.
    result = speech_synthesizer.speak_text_async(text).get()

    # Checks result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized to speaker for text [{}]".format(text))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        print("Did you update the subscription info?")