vacancy_forgot_password_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "result": {
            "type": "boolean"
        },
        "notification_type": {
            "type": "string"
        }
    },
    "required": [
        "result",
        "notification_type"
    ]
}

vacancies_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
        "objects": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "canEdit": {
                        "type": "boolean"
                    },
                    "is_closed": {
                        "type": "boolean"
                    },
                    "id": {
                        "type": "number"
                    },
                    "id_client": {
                        "type": "number"
                    },
                    "payment_from": {
                        "type": "number"
                    },
                    "payment_to": {
                        "type": "number"
                    },
                    "date_pub_to": {
                        "type": "number"
                    },
                    "date_archived": {
                        "type": "number"
                    },
                    "date_published": {
                        "type": "number"
                    },
                    "address": {
                        "type": ["string", "null"]
                    },
                    "profession": {
                        "type": "string"
                    },
                    "work": {},
                    "compensation": {},
                    "candidat": {
                        "type": "string"
                    },
                    "metro": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "number"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "id_metro_line": {
                                    "type": "number"
                                }
                            },
                            "required": [
                                "id",
                                "title",
                                "id_metro_line"
                            ]
                        }
                    },
                    "currency": {
                        "type": "string"
                    },
                    "vacancyRichText": {
                        "type": "string"
                    },
                    "covid_vaccination_requirement": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "title": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "title"
                        ]
                    },
                    "moveable": {
                        "type": "boolean"
                    },
                    "agreement": {
                        "type": "boolean"
                    },
                    "anonymous": {
                        "type": "boolean"
                    },
                    "is_archive": {
                        "type": "boolean"
                    },
                    "is_storage": {
                        "type": "boolean"
                    },
                    "type_of_work": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "title": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "title"
                        ]
                    },
                    "place_of_work": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "title": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "title"
                        ]
                    },
                    "education": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "title": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "title"
                        ]
                    },
                    "experience": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "title": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "title"
                        ]
                    },
                    "maritalstatus": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "title": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "title"
                        ]
                    },
                    "children": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "title": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "title"
                        ]
                    },
                    "client": {
                        "type": ["object", "null"],
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "title": {
                                "type": ["string", "null"]
                            },
                            "link": {
                                "type": ["string", "null"],
                            },
                            "industry": {
                                "type": "array",
                                "items": {}
                            },
                            "description": {
                                "type": "string"
                            },
                            "vacancy_count": {
                                "type": "number"
                            },
                            "staff_count": {
                                "type": "string"
                            },
                            "client_logo": {
                                "type": ["string", "null"]
                            },
                            "address": {
                                "type": ["string", "null"]
                            },
                            "addresses": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "addressString": {
                                            "type": ["string", "null"]
                                        },
                                        "latitude": {
                                            "type": ["number", "null"]
                                        },
                                        "longitude": {
                                            "type": ["number", "null"]
                                        },
                                        "phones": {
                                            "type": "array",
                                            "items": {}
                                        }
                                    },
                                    "required": [
                                        "addressString",
                                        "latitude",
                                        "longitude",
                                        "phones"
                                    ]
                                }
                            },
                            "url": {
                                "type": ["string", "null"]
                            },
                            "short_reg": {
                                "type": "boolean"
                            },
                            "is_blocked": {
                                "type": "boolean"
                            },
                            "registered_date": {
                                "type": "number"
                            },
                            "town": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "number"
                                    },
                                    "title": {
                                        "type": "string"
                                    },
                                    "declension": {
                                        "type": "string"
                                    },
                                    "hasMetro": {
                                        "type": "boolean"
                                    },
                                    "genitive": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "id",
                                    "title",
                                    "declension",
                                    "hasMetro",
                                    "genitive"
                                ]
                            }
                        },
                        "required": [
                            "id",
                            "title",
                            "link",
                            "industry",
                            "description",
                            "vacancy_count",
                            "staff_count",
                            "addresses",
                            "short_reg",
                            "is_blocked",
                            "registered_date",
                            "town"
                        ]
                    },
                    "languages": {
                        "type": "array",
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "number"
                                    },
                                    "title": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "id",
                                    "title"
                                ]
                            }
                        }
                    },
                    "driving_licence": {
                        "type": "array",
                        "items": {}
                    },
                    "catalogues": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "number"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "key": {
                                    "type": "number"
                                },
                                "positions": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "id": {
                                                "type": "number"
                                            },
                                            "title": {
                                                "type": "string"
                                            },
                                            "key": {
                                                "type": "number"
                                            }
                                        },
                                        "required": [
                                            "id",
                                            "title",
                                            "key"
                                        ]
                                    }
                                }
                            },
                            "required": [
                                "id",
                                "title",
                                "key",
                                "positions"
                            ]
                        }
                    },
                    "agency": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "title": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "title"
                        ]
                    },
                    "town": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "title": {
                                "type": "string"
                            },
                            "declension": {
                                "type": "string"
                            },
                            "hasMetro": {
                                "type": "boolean"
                            },
                            "genitive": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "title",
                            "declension",
                            "hasMetro",
                            "genitive"
                        ]
                    },
                    "already_sent_on_vacancy": {
                        "type": "boolean"
                    },
                    "rejected": {
                        "type": "boolean"
                    },
                    "response_info": {
                        "type": "array",
                        "items": {}
                    },
                    "phone": {
                        "type": ["string", "null"]
                    },
                    "fax": {},
                    "faxes": {},
                    "client_logo": {
                        "type": ["string", "null"]
                    },
                    "highlight": {
                        "type": "boolean"
                    },
                    "age_from": {
                        "type": "number"
                    },
                    "age_to": {
                        "type": "number"
                    },
                    "gender": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "title": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "title"
                        ]
                    },
                    "firm_name": {
                        "type": "string"
                    },
                    "firm_activity": {
                        "type": "string"
                    },
                    "link": {
                        "type": "string"
                    },
                    "latitude": {
                        "type": ["number", "null"]
                    },
                    "longitude": {
                        "type": ["number", "null"]
                    }
                },
                "required": [
                    "canEdit",
                    "is_closed",
                    "id",
                    "id_client",
                    "payment_from",
                    "payment_to",
                    "date_pub_to",
                    "date_archived",
                    "date_published",
                    "profession",
                    "work",
                    "compensation",
                    "candidat",
                    "metro",
                    "currency",
                    "vacancyRichText",
                    "covid_vaccination_requirement",
                    "moveable",
                    "agreement",
                    "anonymous",
                    "is_archive",
                    "is_storage",
                    "type_of_work",
                    "place_of_work",
                    "education",
                    "experience",
                    "maritalstatus",
                    "children",
                    "client",
                    "languages",
                    "driving_licence",
                    "catalogues",
                    "agency",
                    "town",
                    "already_sent_on_vacancy",
                    "rejected",
                    "response_info",
                    "fax",
                    "faxes",
                    "highlight",
                    "age_from",
                    "age_to",
                    "gender",
                    "firm_name",
                    "firm_activity",
                    "link"
                ]
            }
        },
        "total": {
            "type": "number"
        },
        "more": {
            "type": "boolean"
        },
        "subscription_id": {
            "type": "number"
        },
        "subscription_active": {
            "type": "boolean"
        }
    },
    "required": [
        "objects",
        "total",
        "more",
        "subscription_id",
        "subscription_active"
    ]
}

vacancy_id_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "canEdit": {
            "type": "boolean"
        },
        "is_closed": {
            "type": "boolean"
        },
        "id": {
            "type": "integer"
        },
        "id_client": {
            "type": "integer"
        },
        "payment_from": {
            "type": "integer"
        },
        "payment_to": {
            "type": "integer"
        },
        "date_pub_to": {
            "type": "integer"
        },
        "date_archived": {
            "type": "integer"
        },
        "date_published": {
            "type": "integer"
        },
        "address": {
            "type": "null"
        },
        "profession": {
            "type": "string"
        },
        "work": {
            "type": "null"
        },
        "compensation": {
            "type": "null"
        },
        "candidat": {
            "type": "string"
        },
        "metro": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "title": {
                            "type": "string"
                        },
                        "id_metro_line": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "id",
                        "title",
                        "id_metro_line"
                    ]
                }
            ]
        },
        "currency": {
            "type": "string"
        },
        "vacancyRichText": {
            "type": "string"
        },
        "covid_vaccination_requirement": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "title"
            ]
        },
        "moveable": {
            "type": "boolean"
        },
        "agreement": {
            "type": "boolean"
        },
        "anonymous": {
            "type": "boolean"
        },
        "is_archive": {
            "type": "boolean"
        },
        "is_storage": {
            "type": "boolean"
        },
        "type_of_work": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "title"
            ]
        },
        "place_of_work": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "title"
            ]
        },
        "education": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "title"
            ]
        },
        "experience": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "title"
            ]
        },
        "maritalstatus": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "title"
            ]
        },
        "children": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "title"
            ]
        },
        "client": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                },
                "link": {
                    "type": "string"
                },
                "industry": {
                    "type": "array",
                    "items": {}
                },
                "description": {
                    "type": "string"
                },
                "vacancy_count": {
                    "type": "integer"
                },
                "staff_count": {
                    "type": "string"
                },
                "client_logo": {
                    "type": "string"
                },
                "address": {
                    "type": "string"
                },
                "addresses": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "addressString": {
                                    "type": "string"
                                },
                                "latitude": {
                                    "type": "number"
                                },
                                "longitude": {
                                    "type": "number"
                                },
                                "phones": {
                                    "type": "array",
                                    "items": {}
                                }
                            },
                            "required": [
                                "addressString",
                                "latitude",
                                "longitude",
                                "phones"
                            ]
                        }
                    ]
                },
                "url": {
                    "type": "string"
                },
                "short_reg": {
                    "type": "boolean"
                },
                "is_blocked": {
                    "type": "boolean"
                },
                "registered_date": {
                    "type": "integer"
                },
                "town": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "title": {
                            "type": "string"
                        },
                        "declension": {
                            "type": "string"
                        },
                        "hasMetro": {
                            "type": "boolean"
                        },
                        "genitive": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "title",
                        "declension",
                        "hasMetro",
                        "genitive"
                    ]
                }
            },
            "required": [
                "id",
                "title",
                "link",
                "industry",
                "description",
                "vacancy_count",
                "staff_count",
                "client_logo",
                "address",
                "addresses",
                "url",
                "short_reg",
                "is_blocked",
                "registered_date",
                "town"
            ]
        },
        "languages": {
            "type": "array",
            "items": {}
        },
        "driving_licence": {
            "type": "array",
            "items": {}
        },
        "catalogues": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "title": {
                            "type": "string"
                        },
                        "key": {
                            "type": "integer"
                        },
                        "positions": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "key": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "key"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "key": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "key"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "id",
                        "title",
                        "key",
                        "positions"
                    ]
                }
            ]
        },
        "agency": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "title"
            ]
        },
        "town": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                },
                "declension": {
                    "type": "string"
                },
                "hasMetro": {
                    "type": "boolean"
                },
                "genitive": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "title",
                "declension",
                "hasMetro",
                "genitive"
            ]
        },
        "already_sent_on_vacancy": {
            "type": "boolean"
        },
        "rejected": {
            "type": "boolean"
        },
        "response_info": {
            "type": "array",
            "items": {}
        },
        "phone": {
            "type": "string"
        },
        "phones": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "number": {
                            "type": "string"
                        },
                        "additionalNumber": {
                            "type": "null"
                        }
                    },
                    "required": [
                        "number",
                        "additionalNumber"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "number": {
                            "type": "string"
                        },
                        "additionalNumber": {
                            "type": "null"
                        }
                    },
                    "required": [
                        "number",
                        "additionalNumber"
                    ]
                }
            ]
        },
        "fax": {
            "type": "null"
        },
        "faxes": {
            "type": "null"
        },
        "client_logo": {
            "type": "string"
        },
        "highlight": {
            "type": "boolean"
        },
        "age_from": {
            "type": "integer"
        },
        "age_to": {
            "type": "integer"
        },
        "gender": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "title"
            ]
        },
        "firm_name": {
            "type": "string"
        },
        "firm_activity": {
            "type": "string"
        },
        "link": {
            "type": "string"
        },
        "video": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "url": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                }
            },
            "required": [
                "id",
                "url",
                "type"
            ]
        },
        "latitude": {
            "type": "null"
        },
        "longitude": {
            "type": "null"
        }
    },
    "required": [
        "canEdit",
        "is_closed",
        "id",
        "id_client",
        "payment_from",
        "payment_to",
        "date_pub_to",
        "date_archived",
        "date_published",
        "address",
        "profession",
        "work",
        "compensation",
        "candidat",
        "metro",
        "currency",
        "vacancyRichText",
        "covid_vaccination_requirement",
        "moveable",
        "agreement",
        "anonymous",
        "is_archive",
        "is_storage",
        "type_of_work",
        "place_of_work",
        "education",
        "experience",
        "maritalstatus",
        "children",
        "client",
        "languages",
        "driving_licence",
        "catalogues",
        "agency",
        "town",
        "already_sent_on_vacancy",
        "rejected",
        "response_info",
        "phone",
        "phones",
        "fax",
        "faxes",
        "client_logo",
        "highlight",
        "age_from",
        "age_to",
        "gender",
        "firm_name",
        "firm_activity",
        "link",
        "video",
        "latitude",
        "longitude"
    ]
}

invalid_token_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "error": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "integer"
                },
                "message": {
                    "type": "string"
                },
                "error": {
                    "type": "string"
                }
            },
            "required": [
                "code",
                "message",
                "error"
            ]
        }
    },
    "required": [
        "error"
    ]
}

invalid_unblock_company_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "error": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "integer"
                },
                "message": {
                    "type": "string"
                }
            },
            "required": [
                "code",
                "message"
            ]
        }
    },
    "required": [
        "error"
    ]
}
